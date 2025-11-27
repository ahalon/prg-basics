file_names = {
    'original_file': 'healthy_lifestyle.txt',
    'target_file': 'copy_healthy_lifestyle.txt'
}


with open(file_names['original_file'], 'r') as original:
    content = original.read()


with open(file_names['target_file'], 'w') as target:
    target.write(content)