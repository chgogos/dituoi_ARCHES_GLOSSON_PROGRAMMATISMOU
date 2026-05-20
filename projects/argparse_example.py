import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', '-i', type=str, help='διαδρομή προς αρχείο εισόδου')
    parser.add_argument('--output_file', '-o', type=str, help='διαδρομή προς αρχείο εξόδου')
    args = parser.parse_args()
    
    print('Αρχείο εισόδου:', args.input_file)
    print('Αρχείο εξόδου:', args.output_file)
