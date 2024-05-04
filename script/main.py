import os
import json
import subprocess

def generate_template():
    project_name = input("Enter the name of the project: ")
    project_slug = project_name.lower().replace(" ", "_")
    
    project_dir = os.path.join("projects", project_slug)
    assets_dir = os.path.join(project_dir, "assets")
    markdown_file = os.path.join(project_dir, "content.md")
    cms_file = "cms.json"
    
    os.makedirs(assets_dir, exist_ok=True)
    open(markdown_file, 'a').close()  # Create empty markdown file
    
    # Update or create a key in the JSON file
    if os.path.exists(cms_file):
        with open(cms_file, 'r') as f:
            cms_data = json.load(f)
    else:
        cms_data = {"projects":{}}
    
    cms_data["projects"][project_slug] = {"name": project_name}
    
    with open(cms_file, 'w') as f:
        json.dump(cms_data, f, indent=4)
    
    print("Template directory created for project '{}'.\n"
          "Add images to '{}' and write content in '{}'.".format(project_name, assets_dir, markdown_file))


def prepare_project():
    cms_file = "cms.json"
    
    if not os.path.exists(cms_file):
        print("No projects found. Please generate a template directory first.")
        return
    
    with open(cms_file, 'r') as f:
        cms_data = json.load(f)
    
    # List available projects
    print("Available projects:")
    for i, (project_slug, project_data) in enumerate(cms_data.items(), start=1):
        project_name = project_data.get("name", "")
        print("{}. {}".format(i, project_name))
    
    # Ask user to choose a project to edit
    project_index = int(input("Enter the number of the project to edit: ")) - 1
    project_slug = list(cms_data.keys())[project_index]
    project_data = cms_data[project_slug]
    project_name = project_data.get("name", "")
    
    # Proceed with editing the selected project
    project_dir = os.path.join("projects", project_slug)
    assets_dir = os.path.join(project_dir, "assets")
    compressed_dir = os.path.join(assets_dir, "compressed")
    markdown_file = os.path.join(project_dir, "content.md")
    
    # Check if assets folder exists
    if not os.path.exists(assets_dir):
        print("Error: Assets folder not found for project '{}'. "
              "Please make sure the 'assets' folder exists.".format(project_name))
        return
    
    # Compress/resize images
    os.makedirs(compressed_dir, exist_ok=True)
    image_files = [f for f in os.listdir(assets_dir) if os.path.isfile(os.path.join(assets_dir, f))]
    for image_file in image_files:
        subprocess.run(["convert", os.path.join(assets_dir, image_file), "-resize", "50%", os.path.join(compressed_dir, image_file)])
    
    # Prompt user to select main picture
    print("Current main picture: {}".format(project_data.get("main_picture", "None")))
    main_picture = input("Enter new main picture (press Enter to keep current): ").strip()
    if not main_picture:
        main_picture = project_data.get("main_picture", "")
    
    # Prompt user to update captions for images
    captions = project_data.get("captions", {})
    for image_file in list(captions.keys()):
        if image_file not in image_files:
            del captions[image_file]
    
    for image_file in image_files:
        print("Current caption for '{}': {}".format(image_file, captions.get(image_file, "No caption")))
        new_caption = input("Enter new caption for '{}' (press Enter to keep current): ".format(image_file)).strip()
        if new_caption:
            captions[image_file] = new_caption
        elif image_file not in captions:
            captions[image_file] = ""
    
    # Prompt user to update video URL
    print("Current video URL: {}".format(project_data.get("video_url", "None")))
    video_url = input("Enter new video URL (press Enter to keep current): ").strip()
    if not video_url:
        video_url = project_data.get("video_url", "")

    
    # Convert markdown file to HTML
    with open(markdown_file, 'r') as f:
        markdown_content = f.read()
    html_content = "{}".format(markdown_content)
    
    # Update project data in JSON file
    project_data["main_picture"] = main_picture
    project_data["captions"] = captions
    project_data["video_url"] = video_url
    project_data["html_content"] = html_content
    
    cms_data[project_slug] = project_data
    
    # Save updated JSON file
    with open(cms_file, 'w') as f:
        json.dump(cms_data, f, indent=4)
    
    print("Project preparation complete.")

def generate_website():
    cms_file = "cms.json"
    
    if not os.path.exists(cms_file):
        print("No projects found. Please generate a template directory first.")
        return
    
    with open(cms_file, 'r') as f:
        cms_data = json.load(f)
    
    for project_slug, project_data in cms_data.items():
        project_dir = os.path.join("projects", project_slug)
        html_file = os.path.join(project_dir, "index.html")
        
        # Generate HTML file for each project
        with open(html_file, 'w') as f:
            f.write(project_data["html_content"])
    
    print("Website generation complete.")

def main():
    print("Select an option:")
    print("1. Generate a template directory for each project")
    print("2. Prepare a project by scanning the directory")
    print("3. Generate the actual website from the JSON")
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == '1':
        generate_template()
    elif choice == '2':
        prepare_project()
    elif choice == '3':
        generate_website()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
