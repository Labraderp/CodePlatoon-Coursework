class ContactList:

    def __init__ (self, list_name, contact_list):
        self.list_name = list_name
        self.contact_list = contact_list

    def add_contact(self, contact_info):
        return self.contact_list.append(contact_info)
    
    def remove_contact(self, name):
        index = 0
        for contacts in self.contact_list:
            if contacts["name"] == name:
                self.contact_list.remove(self.contact_list[index])
            index += 1

    def find_shared_contacts(self, other_contact_list):
        new_list = []
        
        for contacts in self.contact_list:
            if contacts in other_contact_list.contact_list:
                new_list.append(contacts)

        return ContactList("Shared List", new_list)

#Test loops
contacts = [{"name" : "Alice", "num" : 123}, {"name" : "Bob", "num" : 456}]
friends_list = ContactList("Friends", contacts)

print(friends_list.contact_list)

friends_list.add_contact({"name" : "Charlie", "num" : 789})

print(friends_list.contact_list)

new_contacts = ContactList("old friends", [{"name" : "Charlie", "num" : 789}])

friends_list.remove_contact("Alice")
print(friends_list.contact_list)

combined_list = friends_list.find_shared_contacts(new_contacts)

print(combined_list.contact_list)