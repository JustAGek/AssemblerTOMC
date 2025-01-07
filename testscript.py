from assembler import Assembler

INPUT_FILE = 'testcode.asm'
OUT_FILE = 'testcode.mc'
MRI_FILE = 'mri.txt'
RRI_FILE = 'rri.txt'
IOI_FILE = 'ioi.txt'

if __name__ == "__main__":
    bin_text = ''
    asm = Assembler(asmpath=INPUT_FILE, 
                    mripath=MRI_FILE, 
                    rripath=RRI_FILE, 
                    ioipath=IOI_FILE)
    print('Assembling...')
    binaries = asm.assemble()
    for lc in sorted(binaries):
        bin_text += f"{lc}  {binaries[lc]}\n"
    with open('generated_output.mc', 'w') as f:
        f.write(bin_text)
    try:
        with open(OUT_FILE, 'r') as f:
            expected_output = f.read()
        if expected_output.strip() == bin_text.strip():
            print('TEST PASSED')
        else:
            print('TEST FAILED')
            print('Expected Output:')
            print(expected_output)
            print('Generated Output:')
            print(bin_text)
    except FileNotFoundError:
        print(f'Error: Expected output file {OUT_FILE} not found.')
