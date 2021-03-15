import random

#Doubly Circular Linked List
class Node:
    #has information of itself, as well as a pointer to the next node
    def __init__(self, stuff, next_node=None, prev_node=None):
        self.stuff = stuff
        self.next = next_node
        self.prev = prev_node

    def __repr__(self):
        return str(self.stuff)

#took init and repr from Joe, as well as the idea to use Node import
class DoublyLinkedList:
    """
    A Circular Doubly Linked List Function Specialized for the purpose of this simulation
    It's arguments are to take data for it's nodes in the list.
    This is a horrible explanation, I know.
    """
    def __init__(self, *args):
        self.head = None
        self.tail = None
        if args:
            nodes = [Node(arg) for arg in args]
            #creates nodes in list
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
                nodes[i + 1].prev = nodes[i]
            self.head = nodes[0]
            self.tail = nodes[-1]

    def __repr__(self):
        current_node = self.head
        results = ''
        while current_node != self.tail:
            results += str(current_node) + '\n'
            current_node = current_node.next
        results += str(self.tail) + '\n'
        return results

    #add head was not used, this conserves lines

    def add_tail(self, new_node):
        new_node = Node(new_node)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
            new_node.prev = self.tail
            new_node.next = self.head
        else:
            #set the current tail's next and the new nodes prev to the current tail
            self.tail.next = new_node
            new_node.prev = self.tail
            #set the new nodes next to head and then set it to the new tail
            new_node.next = self.head
            self.tail = new_node
            #set head's previous to the new node
            self.head.prev = new_node

    #only pops head, this is because this removes roughly 100 lines by doing it this way
    def popHead(self):
        result = self.head
        self.head = self.head.next
        self.head.prev = self.tail
        return result

    def cycle(self,cycles = 1):
        for i in range(cycles):
            self.add_tail(self.popHead())


def SignSimulation(sign_cycle, read_mean, read_sd, slide_count, days_per_week, student_count):
    """
    Sign Cycle = Amount of seconds to cycle through one slide
    Read Mean = The mean time people are able to read the sign
    Read SD = The standard deviation for the time reading
    Slide Count = The amount of slides on the sign total
    Days Per Week = Days each student arrives per week
    Student Count = Amount of students to be accounted for
    """
    print("Sign Simulation:")
    total_real_seen_collective = []
    collective_percentage = []

    #Sim per student
    for stud_num in range(student_count):
        print(f"\n\n    Student {stud_num}:")

        #Creates circular list of length desired
        Sign = DoublyLinkedList()
        for i in range(slide_count):
            Sign.add_tail(i)

        total_seen = []
        #Sim per day
        for i in range(days_per_week):
            print(f"        Day {i+1}:")

            seen_for = random.gauss(read_mean, read_sd)
            print(f"            Seconds Sign Seen: {seen_for}")

            what_slide_starts = random.randint(0,slide_count-1)
            print(f"            Starting on slide: {what_slide_starts}")

            where_in_current_slide = random.uniform(0,sign_cycle)
            print(f"            Seconds started into cycle of slide: {where_in_current_slide}")

            #aligns head with the start of the cycle
            while str(what_slide_starts) != str(Sign.head):
                Sign.cycle()
    
            #inverses time to no time for time in
            time_left_in_start = sign_cycle - where_in_current_slide

            #Seen Simulation
            total_time = 0
            day_list = []
            added_time = time_left_in_start
            while total_time < seen_for:
                day_list.append(Sign.head)
                Sign.cycle()
                #adds time left from original slide on first run, but makes it the time each slide goes for on each subsequent run
                total_time += added_time
                added_time = sign_cycle
            print(f"            Slides seen: {day_list}")

            #appends to the total list
            for i in day_list:
                total_seen.append(int(str(i)))

        #gets rid of duplicates for total_real_seen
        total_real_seen = []
        for i in total_seen:
            if i not in total_real_seen:
                total_real_seen.append(int(i))
        total_real_seen.sort()

        #final percentage calculation
        percentage_seen = (len(total_real_seen) / slide_count)*100

        print(f"\n    Original List Seen: {total_seen}\n    List after duplicates removed: {total_real_seen}\n    Percentage Seen by Student {stud_num}: %{percentage_seen}")
        
        #adds total amount seen to total list
        for i in total_real_seen:
            total_real_seen_collective.append(i)

        #adds total percentage seen to list
        collective_percentage.append(percentage_seen)


    total_real_seen_collective_sorted = []
    for i in total_real_seen_collective:
        if i not in total_real_seen_collective_sorted:
            total_real_seen_collective_sorted.append(int(i))
    total_real_seen_collective_sorted.sort()

    print(f"\n\nOverall Results:\n    Total Seen: {total_real_seen_collective_sorted}")

    #gives percentage of students that have seen each individual slide
    for i in range(slide_count):
        seen_count = []
        for j in total_real_seen_collective:
            if i == j:
                seen_count.append(j)
    
        percentage_students_slide_seen = (len(seen_count) / student_count)*100

        print(f"        Slide {i} percentage of students seen: %{percentage_students_slide_seen}")

    #percentage seen by students collectively
    percentage_of_slides_seen_by_students = (len(total_real_seen_collective_sorted) / slide_count)*100
    print(f"    Percentage of slides seen by student body: %{percentage_of_slides_seen_by_students}")


    #average of collective
    total_before_divide = 0
    for i in collective_percentage:
        total_before_divide += i
    average_amount_of_slides_seen_by_student_body = total_before_divide / len(collective_percentage)
    print(f"    Average of percentages of slides each student saw: %{average_amount_of_slides_seen_by_student_body}")


#taking input
sign_cycle_in = int(input("How many seconds does 1 slide stay on for?\n"))
read_mean_in = int(input("What is the mean amount of seconds someone will typically see the sign?\n"))
read_sd_in = int(input("What is the standard deviation of said amount of seconds?\n"))
slide_count_in = int(input("How many slides appear on the sign?\n"))
days_per_week_in = int(input("How many days does a student appear per week?\n"))
student_count_in = int(input("How many students do you want to run this simulation for?\n"))
print("\n\n")

while(True):
    input("\n\nRun? (Press Enter)\n")
    SignSimulation(sign_cycle_in,read_mean_in,read_sd_in,slide_count_in,days_per_week_in,student_count_in)

