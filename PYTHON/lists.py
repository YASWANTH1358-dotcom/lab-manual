#lists full concept
names = ["dhoni","kolhi","rohit","ruturaj","rahul"];
#index
print(names[1]);
print(names[-1]);
#slicing
print(names[1:4]);
print(names[:3]);
print(names[1: ]);
print(names[::5]);
#add_elements
names.append("bravo");
print(names);
names.insert(2,"strokes");
names.extend(["jadeja","hardik","bhuvi"]);
print(names);
#remove_elements
names.remove("bhuvi");
