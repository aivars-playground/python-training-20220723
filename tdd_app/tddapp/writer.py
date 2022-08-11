def local(infile, outfile):
    with infile, outfile:
        outfile.write(infile.read())


def s3(client, infile, bucket_name, file_name):
    client.upload_fileobj(infile, bucket_name, file_name)
