import os
import json
import subprocess
import markdown
from jinja2 import Environment, FileSystemLoader

def generate_template():
    project_name = input("Enter the name of the project: ")
    project_slug = project_name.lower().replace(" ", "_")
    
    project_dir = os.path.join("website/projects", project_slug)
    en_dir = os.path.join(project_dir, "en")
    assets_dir = os.path.join(project_dir, "assets")
    markdown_file = os.path.join(project_dir, "content.md")
    markdown_en_file = os.path.join(en_dir, "content.md")
    cms_file = "cms.json"
    
    os.makedirs(en_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    open(markdown_file, 'a').close()  # Create empty markdown files
    open(markdown_en_file, 'a').close() 

    # Update or create a key in the JSON file
    if os.path.exists(cms_file):
        with open(cms_file, 'r') as f:
            cms_data = json.load(f)
    else:
        os.makedirs("website/en", exist_ok=True)
        cms_data = {"projects":{}, "categories":[]}  # Initialize categories list
    
    cms_data["projects"][project_slug] = {"name": project_name}
    
    with open(cms_file, 'w') as f:
        json.dump(cms_data, f, indent=4)
    
    print("Template directory created for project '{}'.\n"
          "Add images to '{}' and write content in '{}'.".format(project_name, assets_dir, markdown_file))


def add_categories_to_cms():
    cms_file = "cms.json"
    
    if not os.path.exists(cms_file):
        print("No projects found. Please generate a template directory first.")
        return
    
    with open(cms_file, 'r') as f:
        cms_data = json.load(f)
    
    categories = cms_data.get("categories", [])
    category = input("Enter the name of the category to add: ")
    categories.append(category)
    
    cms_data["categories"] = categories
    
    with open(cms_file, 'w') as f:
        json.dump(cms_data, f, indent=4)
    
    print("Category '{}' added to CMS.".format(category))



def prepare_project():
    cms_file = "cms.json"
    
    if not os.path.exists(cms_file):
        print("No projects found. Please generate a template directory first.")
        return
    
    with open(cms_file, 'r') as f:
        cms_data = json.load(f)
    
    # Check if categories exist
    if not cms_data.get("categories"):
        print("Error: No categories found in the CMS.")
        return
    
    # List available projects
    print("Available projects:")
    for i, (project_slug, project_data) in enumerate(cms_data["projects"].items(), start=1):
        project_name = project_data.get("name", "")
        print("{}. {}".format(i, project_name))
    
    # Ask user to choose a project to edit
    project_index = int(input("Enter the number of the project to edit: ")) - 1
    project_slug = list(cms_data["projects"].keys())[project_index]
    project_data = cms_data["projects"][project_slug]
    project_name = project_data.get("name", "")
    
    # List available categories
    print("Available categories:")
    for i, category in enumerate(cms_data["categories"], start=1):
        print("{}. {}".format(i, category))
    
    # Check if there are no categories
    if not cms_data["categories"]:
        print("Error: No categories found in the CMS.")
        return
    
    # Ask user to choose a category
    category_index = int(input("Enter the number of the category to assign to the project: ")) - 1
    selected_category = cms_data["categories"][category_index]
    
    # Update project data with the selected category
    project_data["category"] = selected_category
    
    # Proceed with editing the selected project
    project_dir = os.path.join("website/projects", project_slug)
    en_dir = os.path.join(project_dir, "en")
    assets_dir = os.path.join(project_dir, "assets")
    compressed_dir = os.path.join(assets_dir, "compressed")
    markdown_file = os.path.join(project_dir, "content.md")
    markdown_en_file = os.path.join(en_dir, "content.md")

    # Check if assets folder exists
    if not os.path.exists(assets_dir):
        print("Error: Assets folder not found for project '{}'. "
              "Please make sure the 'assets' folder exists.".format(project_name))
        return
    
    # Check if there are no pictures in the assets folder
    if not os.listdir(assets_dir):
        print("Error: No pictures found in the 'assets' folder for project '{}'."
              " Please add pictures before proceeding.".format(project_name))
        return
    
    # Compress/resize images
    os.makedirs(compressed_dir, exist_ok=True)
    image_files = [f for f in os.listdir(assets_dir) if os.path.isfile(os.path.join(assets_dir, f))]
    for image_file in image_files:
        subprocess.run(["convert", os.path.join(assets_dir, image_file), "-resize", "50%", os.path.join(compressed_dir, image_file)])
    
    # Prompt user to select main picture
    print("Available pictures:")
    for i, image_file in enumerate(image_files, start=1):
        print("{}. {}".format(i, image_file))
    print("Enter the number of the main picture (or press Enter to keep current): ")
    main_picture_index = input()
    if main_picture_index:
        main_picture_index = int(main_picture_index) - 1
        if 0 <= main_picture_index < len(image_files):
            main_picture = image_files[main_picture_index]
        else:
            print("Invalid picture number. Keeping current main picture.")
            main_picture = project_data.get("main_picture", "")
    else:
        main_picture = project_data.get("main_picture", "")
    
    # Prompt user to update captions for images
    captions_it = project_data.get("captions_it", {})
    captions_en = project_data.get("captions_en", {})
    for image_file in image_files:
        print("Current caption for '{}' (Italian): {}".format(image_file, captions_it.get(image_file, "No caption")))
        new_caption_it = input("Enter new caption for '{}' (Italian) (press Enter to keep current): ".format(image_file)).strip()
        if new_caption_it:
            captions_it[image_file] = new_caption_it
        elif image_file not in captions_it:
            captions_it[image_file] = ""
        
        print("Current caption for '{}' (English): {}".format(image_file, captions_en.get(image_file, "No caption")))
        new_caption_en = input("Enter new caption for '{}' (English) (press Enter to keep current): ".format(image_file)).strip()
        if new_caption_en:
            captions_en[image_file] = new_caption_en
        elif image_file not in captions_en:
            captions_en[image_file] = ""
    
    # Prompt user to update video URL
    print("Current video URL: {}".format(project_data.get("video_url", "None")))
    video_url = input("Enter new video URL (press Enter to keep current): ").strip()
    if not video_url:
        video_url = project_data.get("video_url", "")

    # Convert markdown file to HTML for Italian
    with open(markdown_file, 'r') as f:
        markdown_content_it = f.read()
        markdown_content_it = markdown.markdown(markdown_content_it)
    html_content_it = markdown_content_it
    
    # Convert markdown file to HTML for English
    with open(markdown_en_file, 'r') as f:
        markdown_content_en = f.read()
        markdown_content_en = markdown.markdown(markdown_content_en)
    html_content_en = markdown_content_en
 
    # Update project data in JSON file
    project_data["main_picture"] = main_picture
    project_data["captions_it"] = captions_it
    project_data["captions_en"] = captions_en
    project_data["video_url"] = video_url
    project_data["html_content_it"] = html_content_it
    project_data["html_content_en"] = html_content_en
    
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

    # markdown misc content 
    misc_content_en = {}
    misc_content_it = {}

    # Get a list of Markdown files in the 'en' folder
    markdown_files_en = [f for f in os.listdir('misc/en') if f.endswith('.md')]

    # Iterate through each Markdown file in the 'en' folder
    for file_name in markdown_files_en:
        file_path = os.path.join('misc/en', file_name)

        # Read the content of the Markdown file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Convert Markdown content to HTML
        html_content = markdown.markdown(content)

        # Store the HTML content in the dictionary with the file name as the key
        misc_content_en[file_name.replace('.md','')] = html_content

    # Get a list of Markdown files in the 'it' folder
    markdown_files_it = [f for f in os.listdir('misc/it') if f.endswith('.md')]

    # Iterate through each Markdown file in the 'it' folder
    for file_name in markdown_files_it:
        file_path = os.path.join('misc/it', file_name)

        # Read the content of the Markdown file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Convert Markdown content to HTML
        html_content = markdown.markdown(content)

        # Store the HTML content in the dictionary with the file name as the key
        misc_content_it[file_name.replace('.md','')] = html_content


    # Get gallery images
    gallery_pics = [f for f in os.listdir('website/galleria') if not f.startswith('.')]

    # Initialize Jinja environment
    env = Environment(loader=FileSystemLoader('.'))
    
    # Render index page
    # In italian
    index_template_it = env.get_template('template/index_template.html')
    index_html_it = index_template_it.render(cms_data=cms_data, gallery_pics=gallery_pics, misc_content=misc_content_it)

    with open('website/index.html', 'w') as index_file:
        index_file.write(index_html_it)

    # In english
    index_template_en = env.get_template('template/index_template_en.html')
    index_html_en = index_template_en.render(cms_data=cms_data, gallery_pics=gallery_pics, misc_content=misc_content_en)

    with open('website/en/index.html', 'w') as index_file:
        index_file.write(index_html_en)
    

    # Render project pages

    # In Italian
    project_template = env.get_template('template/project_template.html')
    
    for project, values in cms_data["projects"].items():
        project_html = project_template.render(values=values, cms_data=cms_data, misc_content=misc_content_it)
        project_dir = os.path.join("website/projects", project)
        with open(os.path.join(project_dir, "index.html"), 'w') as project_file:
            project_file.write(project_html)

    # In english
    project_template_en = env.get_template('template/project_template_en.html')
        
    for project, values in cms_data["projects"].items():
        project_html = project_template_en.render(values=values, cms_data=cms_data, misc_content=misc_content_en)
        project_dir = os.path.join("website/projects/", project,'en/')
        with open(os.path.join(project_dir, "index.html"), 'w') as project_file:
            project_file.write(project_html)
    
    print("Website generation complete.")


def main():
    print("Select an option:")
    print("1. Generate a template directory")
    print("2. Prepare a project by scanning the directory")
    print("3. Add categories")
    print("4. Generate the website")
    print("5. Exit")
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    
    if choice == '1':
        generate_template()
    elif choice == '2':
        prepare_project()
    elif choice == '3':
        add_categories_to_cms()
    elif choice == '4':
        generate_website()
    elif choice == '5':
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
