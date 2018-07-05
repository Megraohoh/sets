# Create an empty set named showroom
showroom = set()
# Add four of your favorite car model names to the set
showroom.update(["Tesla Model S", "Tesla Model X", "Bugatti Veyron 16.4", "Honda Element"])
# Print the length of your set
print(len(showroom))
# Pick one of the items in your show room and add it to the set again
showroom.add("Tesla Model S") 
# Print your showroom. Notice how there's still only one instance of that model in there
print(showroom)
# Using update(), add two more car models to your showroom with another set
showroom.update({"Ford Pinto", "Mullet Mobile"})
print(showroom)
# You've sold one of your cars. Remove it from the set with the discard() method
showroom.discard("Mullet Mobile")
showroom.discard("Tesla Model X")
print(showroom)

# Now create another set of cars in a variable junkyard. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = set(["Ford Pinto", "Nissan Altima", "Tesla Model S", "Ford Escape"])
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print(showroom.intersection(junkyard))
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
print(showroom.union(junkyard))
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
print(showroom.discard(junkyard))