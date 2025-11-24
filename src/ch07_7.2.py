# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # Remove leading/trailing whitespace including newline character
    line = line.rstrip()
    # Split the line into words
    fields = line.split()
    # The second word is the confidence value
    confidence = fields[1]
    # Convert the confidence value to a floating point number
    fconfidence = float(confidence)
    # Update count and total
    count = count + 1
    total = total + fconfidence
    # Calculate and print the average
    average = total / count
print("Average spam confidence:", average)

