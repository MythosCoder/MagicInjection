#!/usr/bin/python3

import argparse
from pathvalidate import is_valid_filename
from sys import exit
from binascii import unhexlify
from os.path import exists

EXTENSIONS_BITLIST = {
	"jpeg" : ['00', '00', '00', '0C', '6A', '50', '20', '20', '0D', '0A'],
	"png" : ['89', '50', '4e', '47', '0d', '0a', '1a', '0a', '00', '00', '00', '0d', '49', '48', '44', '52'],
	"gif" : ['47', '49', '46', '38', '37', '61'],
	"mp3" : ['FF', 'FB'],
	"pdf" : ['25', '50', '44', '46', '2d', '31', '2e', '34'],
	"doc" : ['D0', 'CF', '11', 'E0', 'A1', 'B1', '1A', 'E1'],
	"pdf" : ['25', '50', '44', '46', '2d', '31', '2e', '34'],
	"xml" : ['3c', '3f', '78', '6d', '6c', '20'],
	"zip" : ['50', '4B', '05', '06'],
	"rar" : ['52', '61', '72', '21', '1A', '07', '00'],
	"7z" : ['37', '7A', 'BC', 'AF', '27', '1C']
}


def parse_arguments() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		prog='MagicInjection',
		description='This program injects magic bytes into files to spoof file types so they can bypass upload mechanisms',
		epilog="'Examples:\n  ./MagicInjection bad.php pdf\n  ./MagicInjection shell.gif --force'",
		formatter_class=argparse.RawTextHelpFormatter
	)

	parser.add_argument('filename', nargs='?', help='Name of the file to be created (e.g., bad.php)')
	parser.add_argument('extension', nargs='?', help='Filetype you want it to spoof as (e.g., png, pdf, doc)')
	parser.add_argument('--list', action='store_true', help='List all supported filetype extensions')
	parser.add_argument('--force', action='store_true', help='Force overwrite if file already exists')
	parser.add_argument('--write', nargs='?', type=int, help="writes 'x' count of zeroes in Megabytes to file (e.g., --write 5 (equals to 5MB writen into file)")

	return parser.parse_args()


def list_supported_extensions() -> None:
	print("Supported file type spoofing extensions:")
	for ext in sorted(EXTENSIONS_BITLIST.keys()):
		print(f" - {ext}")
	exit(0)


def write_magic_bytes(filename: str, extension: str, force: bool) -> None:
	extension = extension.lower()

	if not is_valid_filename(filename):
		print(f"filename not valid. --> {filename}")
		exit(1)

	if extension not in EXTENSIONS_BITLIST:
		print(f"Unsuported extension: {extension}")
		print("Use '--list' to see supported file types")
		exit(1)

	if exists(filename) and not force:
		print(f"File '{filename}' already exists. Use --force to overwrite")
		exit(1)

	print(f"Writing magic bytes for '{extension}' to --> '{filename}'...")
	with open(filename, "wb") as output_file:
		for hex_byte in EXTENSIONS_BITLIST[extension]:
			output_file.write(unhexlify(hex_byte))

	print("Done!")


def main() -> None:
	args = parse_arguments()

	if args.list:
		list_supported_extensions()

	if not args.filename or not args.extension:
		print("Error: 'filename and 'extension' are required unless, you are looking for listing extensions using '--list'")
		print("Use '-h' for help and usage")
		exit(1)

	write_magic_bytes(args.filename, args.extension, args.force)

	if args.write and args.write >= 1:
		print(f"\nWriting {args.write}MB of zeroes to file...")

		# Open the file in write-binary mode
		with open(args.filename, 'wb') as file:
			chunk_bytes = 1024 * 1024  # 1MB chunk size
			chunk = b'\x00' * chunk_bytes  # A chunk of zeroes

			# Write full chunks
			full_chunks = args.write // 1  # Full 1MB chunks
			for _ in range(full_chunks):
				file.write(chunk)

			# Write remaining bytes if any
			remaining_mb = args.write % 1
			if remaining_mb:
				file.write(b'\x00' * (remaining_mb * 1024 * 1024))
		print("Done!")


if __name__ == '__main__':
	main()
