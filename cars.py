# Create an empty set named showroom
showroom = set()
# Add four of your favorite car model names to the set
showroom.update(["Tesla Model S", "Tesla Model X", "Bugatti Veyron 16.4", "Honda Element"])
# Print the length of your set
print("this is length of showroom" , len(showroom))
# Pick one of the items in your show room and add it to the set again
add_duplicate = showroom.add("Tesla Model S") 
# Print your showroom. Notice how there's still only one instance of that model in there
print("Duplicate should be present", showroom)
# Using update(), add two more car models to your showroom with another set
showroom.update({"Ford Pinto", "Mullet Mobile"})
print("There should be 6 cars", showroom)
# You've sold one of your cars. Remove it from the set with the discard() method
showroom.discard("Mullet Mobile")
showroom.discard("Tesla Model X")
print("2 cars removed, 4 cars listed", showroom)

# Now create another set of cars in a variable junkyard. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = ("Ford Pinto", "Nissan Altima", "Tesla Model S", "Ford Escape")
print("this is junkyard", junkyard)
# Use the intersection method to see which cars exist in both the showroom and the junkyard.
print("Cars in common", showroom.intersection(junkyard))
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
purchased = showroom.union(junkyard)
print("This is the combined set", purchased)
# Use the discard() method to remove any cars that you acquired from the junkyard that you don't want in your showroom.
purchased.discard("Ford Escape")
print("This is all that's left", purchased)