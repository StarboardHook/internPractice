from DocumentConverterFactory import DocumentConverterFactory

file_path =input("Enter the file path: ")
try:
    converter = DocumentConverterFactory.create_converter(file_path)
    content = converter.convert(file_path)
    print("Converted Content:")
    print(content)
except ValueError as e:
    print(e)


