import re

def remove_numbers(file, output_file):
    minute_pattern = re.compile(r'\d{1,2}:\d{2}$')
    with open(file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if re.match(minute_pattern, line):
                lines.remove(line)
            
        
    with open(output_file, 'w') as w:
        w.writelines(lines)


if __name__ == '__main__':
    remove_numbers('transcription.txt', 'filtered_transcription.txt')
        