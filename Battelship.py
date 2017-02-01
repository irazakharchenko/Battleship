def read_field(file):
    '''
    (str) -> (data)
    '''
    with open(file, 'r') as f:
        cont = f.read().strip('\t')
        print(cont[:10])

read_field('field')