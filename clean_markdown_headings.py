import re
import os

# Emojis to keep
allowed_emojis = {'✅', '❌', '⚠️'}

def clean_heading(line):
    # Temporarily replace allowed emojis with placeholders
    for emoji in allowed_emojis:
        placeholder = f'__EMOJI_{hash(emoji)}__'
        line = line.replace(emoji, placeholder)
    # Remove all emojis (unicode ranges)
    line = re.sub(r'[\U0001F300-\U0001FAFF]', '', line)
    # Restore allowed emojis
    for emoji in allowed_emojis:
        placeholder = f'__EMOJI_{hash(emoji)}__'
        line = line.replace(placeholder, emoji)
    # Replace em dash with hyphen
    line = line.replace('—', '-')
    # Remove apostrophes
    line = line.replace("’", "").replace("'", "")
    return line

def process_file(filepath):
    changed = False
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            if line.startswith('#'):
                new_line = clean_heading(line)
                if new_line != line.strip():
                    changed = True
                f.write(new_line + '\n')
            else:
                f.write(line)
    if changed:
        print(f'Cleaned: {filepath}')

def walk_and_process(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.md'):
                process_file(os.path.join(dirpath, file))

if __name__ == '__main__':
    walk_and_process('.')

