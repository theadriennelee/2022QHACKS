from transcriber import transcriber

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')

a = transcriber(r"C:\Users\Admin\Downloads\segmentation.mp4")
print(a)
a.wait()
foo = a.getparagraphs()
start,end = a.gettstamps()

for x in range(len(foo)):
    print(foo[x])
    print('Start: ', start[x])
    print('End: ', end[x])

