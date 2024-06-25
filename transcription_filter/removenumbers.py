import re

def remove_numbers(file, output_file):
    minute_pattern = re.compile(r'\d{1,2}:\d{2}$')
    filtered_lines = []
    with open(file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if not minute_pattern.match(line.strip()):
                filtered_lines.append(line)
            
        
    with open(output_file, 'w') as w:
        w.writelines(filtered_lines)


if __name__ == '__main__':
    remove_numbers('transcription.txt', 'filtered_transcription.txt')
        