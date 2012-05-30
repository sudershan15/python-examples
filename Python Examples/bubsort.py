def bubble_sort(seq):
    """Inefficiently sort the mutable sequence (list) in place.
       seq MUST BE A MUTABLE SEQUENCE.
 
       As with list.sort() and random.shuffle this does NOT return 
    """
    k=0
    changed = True
    while changed:
        changed = False
        print "PASS: " , k+1
        for i in xrange(len(seq) - (k+1)):
            print seq
            if seq[i] > seq[i+1]:
                print "changing ", seq[i],",",seq[i+1]
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
            else:
                print seq[i]," and ", seq[i+1], " already sorted"
        k=k+1
    return None
 
if __name__ == "__main__":
   """Sample usage and simple test suite"""
 
   from random import shuffle
 
   
   testcase = ["celery", "carrot", "cabbage", "tomato","brinjal","potato","chillies"] # make a copy
   bubble_sort(testcase)
   print "FINAL RESULT: "
   print testcase
