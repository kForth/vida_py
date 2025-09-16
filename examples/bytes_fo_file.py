import click


@click.command()
@click.option("--bytestr", "-s", type=click.STRING)
@click.option("--bytefile", "-f", type=click.Path(dir_okay=False, exists=True))
@click.option("--outfile", "-o", type=click.Path(dir_okay=False), default="output.bin")
def main(bytestr, bytefile, outfile):
    """
    Convert a string of bytes to a file.
    """

    if bytefile:
        with open(bytefile, encoding="utf-8") as src:
            bytestr = src.read()

    # Convert the string to bytes
    byte_array = bytes.fromhex(bytestr[2 if bytestr.startswith("0x") else 0 :])

    # Write the bytes to a file
    with open(outfile, "wb") as f:
        f.write(byte_array)

    click.echo(f"Bytes written to {outfile}")


if __name__ == "__main__":
    main()
