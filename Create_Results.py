import numpy as np
import argparse


def extract_vectors(input_file, output_file, dim):
    '''this function takes the name of the input, output files, and the expected length of feature-vector and \
    creats a file of only vectors for each paragraph'''

    vector_list=[]
    with open(input_file, 'r') as f:
        for line in f:
            line_sp=line.rsplit()
            vector=line_sp[-dim:]
            vector = np.array([float(x) for x in vector])
            vector_list.append(vector)

        vector_np = np.array(vector_list)

    np.savetxt(output_file, vector_np)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  help="the file with paragraph+vector(s)", default="out.txt")
    parser.add_argument('--output', help="the file with only vectors", default="vector_results.txt")
    parser.add_argument('--dim', help='dimensions of the wordvec', default=100)
    args = parser.parse_args()
    extract_vectors(input_file=args.input, output_file=args.output, dim=int(args.dim))
