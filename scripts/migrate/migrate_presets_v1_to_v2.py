import json
import os

file_path = r"d:\Users\Luminary\Projects\GitHubProjects\OMaster\app\src\main\assets\presets.json"

def migrate():
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    presets = data.get('presets', [])
    modified_count = 0
    
    # Fields to remove
    fields_to_remove = [
        "iso", "shutterSpeed", "exposureCompensation", 
        "colorTemperature", "colorHue", "whiteBalance", 
        "colorTone", "filter", "softLight", "tone", 
        "saturation", "warmCool", "cyanMagenta", 
        "sharpness", "vignette"
    ]

    for preset in presets:
        is_modified = False
        
        # 1. Remove old fields
        for field in fields_to_remove:
            if field in preset:
                del preset[field]
                is_modified = True
        
        # 2. Migrate mode to tags
        if 'mode' in preset:
            mode_value = preset['mode']
            # Only create tags if mode exists and is not null/empty
            if mode_value:
                # If tags already exist, append; otherwise create new list
                if 'tags' not in preset:
                    preset['tags'] = [mode_value]
                elif mode_value not in preset['tags']:
                    preset['tags'].append(mode_value)
            
            del preset['mode']
            is_modified = True

        # 3. Move shooting tips
        sections = preset.get('sections', [])
        found_tips = False
        tips_content = None
        
        # Find and extract shooting tips
        for section in sections:
            items = section.get('items', [])
            new_items = []
            section_modified = False
            
            for item in items:
                if item.get('label') == '@string/shooting_tips':
                    tips_content = item.get('value')
                    found_tips = True
                    section_modified = True
                else:
                    new_items.append(item)
            
            if section_modified:
                section['items'] = new_items
                is_modified = True
        
        # Clean up empty sections
        original_section_count = len(sections)
        new_sections = [s for s in sections if len(s.get('items', [])) > 0]
        if len(new_sections) < original_section_count:
            preset['sections'] = new_sections
            is_modified = True
        else:
             preset['sections'] = new_sections

        # Add description field if tips found
        if found_tips and tips_content:
            preset['description'] = {
                "title": "Shooting Tips",
                "content": tips_content
            }
            is_modified = True
            print(f"Migrated tips for preset: {preset.get('name')}")

        if is_modified:
            modified_count += 1

    if modified_count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Successfully migrated {modified_count} presets.")
    else:
        print("No presets needed migration.")

if __name__ == "__main__":
    migrate()
