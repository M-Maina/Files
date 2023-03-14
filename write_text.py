def write_content():
    with open('num-series.txt', 'w') as writer:
        for x in range(20):
            content = f'{x}\n'
            writer.write(content)
            
def append_content():
    with open('num-series.txt', 'w') as writer:
        for x in range(20, 30):
            content = f'{x}\n'
            writer.write(content)
if __name__ == '__main__':
    write_content()
    append_content()