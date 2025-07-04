#Combine list1 = [1, 2, 3] and list2 = [4, 5, 6] into a new list and print the result.


def combine_student_batches(batch_a, batch_b):
    for roll in batch_b:
        batch_a.append(roll)
    print("Combined roll numbers:", batch_a)

batch_a = [1, 2, 3]
batch_b = [4, 5, 6]

combine_student_batches(batch_a, batch_b)