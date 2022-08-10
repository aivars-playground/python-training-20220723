def local(infile, outfile):
    with infile, outfile:
        outfile.write(infile.read())
