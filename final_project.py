# final_project.py
# Caleb Oviawe & Imisi Lawal, ENDG 233 F21

import numpy as np
import matplotlib.pyplot as plt

class Country:
    """A class used to create a Country object.

        Attributes:
            country (str): String that represents the country's name
            un region (str): String that represents index 1 of the country index in country data
            un subregion (str): String that represents index 2 of the country index in country data
            countryarea (str): String that represents index 3 of the country index in country data
    """

    def __init__(self, country ,UNregion, UNsubregion, Countryarea ):
        self.country = country 
        self.UNregion = UNregion
        self.UNsubregion = UNsubregion
        self.Countryarea = Countryarea

    def print_all_stats(self):
        """A function that prints the name, un region, un subregion, and area of the country instance.

        Parameters: None
        Return: None

        """
        print("Country Name: {0}, UN Region: {1}, UN Subregion: {2}, Country Area: {3} square kilometres.".format(self.country, self.UNregion, self.UNsubregion, self.Countryarea))

def main():  
 #Imports data from csv fIles
    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', skip_header = True, dtype = str)
    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True, dtype = int)
    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter = ',', skip_header = True, dtype = str)

 #Prints the Array Data
    print('Array for Country Data:')
    print(country_data)
    print('Array for Population Data:')
    print(population_data)
    print('Array for Threatened Species Data:')
    print(threatened_species)

#Creates lists from the coloumns of data in the Country_Data.csv file
    list_of_country_names = list(country_data[:,0])
    list_of_area = list(country_data[:,3])

 #Creates lists from the coloumns of data in the Threatened_Data.csv file
    list_plants = list(threatened_species[:,1])
    list_fish = list(threatened_species[:,2])
    list_birds = list(threatened_species[:,3])
    list_mammals = list(threatened_species[:,4])
 
 #Creates dictionaries from the country data lists
    country_names_to_area = dict(zip(list_of_country_names, list_of_area))

 #Creates dictionaries from the threatened species data
    country_to_plants = dict(zip(list_of_country_names, list_plants))
    country_to_fish = dict(zip(list_of_country_names, list_fish))  
    country_to_birds = dict(zip(list_of_country_names, list_birds))
    country_to_mammals = dict(zip(list_of_country_names, list_mammals))
    
    
    selected_country = input('Hey there! Please enter a country name:') #User inputted country

    num_plants = int(country_to_plants[selected_country]) #Finds the number of fish from the fish dictionary with the selected country
    num_fish = int(country_to_fish[selected_country]) #Finds the number of fish from the fish dictionary with the selected country
    num_birds = int(country_to_birds[selected_country]) #Finds the number of fish from the fish dictionary with the selected country
    num_mammals = int(country_to_mammals[selected_country]) #Finds the number of fish from the fish dictionary with the selected country

    while not selected_country in list_of_country_names: #When the input country isn't contained in data list
        print('You must enter a valid country name.')
        selected_country = input('Please enter country name:') #Asks user to re-enter a valid country

    if selected_country in list_of_country_names:
        country_index = list_of_country_names.index(selected_country)
        population_data_list = list(population_data[country_index])
        population_list = (population_data_list[1:])
        mean_population = int(np.mean(population_list)) #Finds the mean population over the last 21 years for selected country
        max_population = int(np.max(population_list)) #Finds the max population over the last 21 years for selected country
        min_population = int(np.min(population_list)) #Finds the min population over the last 21 years for selected country
        country_class = Country(selected_country, country_data[country_index][1],country_data[country_index][2],country_data[country_index][3])
        country_class.print_all_stats()
        
        print('The mean population of this country from 2000 to 2021 is:', mean_population,'people.')
        print('The max population of this country from 2000 to 2021 is:', max_population,'people.')
        print('The min population of this country from 2000 to 2021 is:', min_population,'people.')

        user_choice = input('Would you like to investigate the threatened species of your selected country? Yes or No:') #Allows user to decide if they wish to continue
        
        while user_choice == 'No' or user_choice == 'Yes':
            if user_choice == 'No':
                break
            elif user_choice == 'Yes':
                print('Great!')
                user_species = input('Please select a desired threatened species to investigate: Plants, Fish, Birds or Mammals:') #Allows user to select a species to investigate
                if user_species == 'Plants':
                    print('There are',num_plants,'threatened species of plants in',selected_country)
                    if num_plants > 0:
                        area = int(country_names_to_area[selected_country])
                        species_density = area // num_plants #Finds the density of threatened species of plants if there are any in selected country
                        print('For every',species_density,'sqaure kilometres of land, there is 1 threatened species.')
                    elif num_plants == 0:
                        break
                
                elif user_species == 'Fish':
                    print('There are',num_fish,'threatened species of fish in',selected_country)
                    if num_fish > 0:
                        area = int(country_names_to_area[selected_country])
                        species_density = area // num_fish #Finds the density of threatened species of fish if there are any in selected country
                        print('For every',species_density,'sqaure kilometres of land, there is 1 threatened species.')
                    elif num_fish == 0:
                        break                
                
                elif user_species == 'Birds':
                    print('There are',num_birds,'threatened species of birds in',selected_country)
                    if num_birds > 0:
                        area = int(country_names_to_area[selected_country])
                        species_density = area // num_birds #Finds the density of threatened species of birds if there are any in selected country
                        print('For every',species_density,'sqaure kilometres of land, there is 1 threatened species.')
                    elif num_birds == 0:
                        break
                
                elif user_species == 'Mammals':
                    print('There are',num_mammals,'threatened species of mammals in',selected_country)
                    if num_mammals > 0:
                        area = int(country_names_to_area[selected_country])
                        species_density = area // num_mammals #Finds the density of threatened species of mammals if there are any in selected country
                        print('For every',species_density,'sqaure kilometres of land, there is 1 threatened species.')
                    elif num_mammals == 0:
                        break
            break
        
       #Makes graphs from code determined data
        y_axis1 = (num_plants,num_fish,num_birds,num_mammals)
        
        x_axis1 = ['Plants' , 'Fish' , 'Birds' , 'Mammals']

        plt.bar(x_axis1,y_axis1) # x is the x axis, y is the y axis
        plt.xlabel('Threatened Species') # x axis label
        plt.ylabel('Number of Species') # y axis label
        plt.title('Threatened Species in Selected Country') #graph title
        plt.show() #displays graph

        x_axis2 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21']
        plt.plot(x_axis2,population_list) # x is the x axis, population_list is the y axis
        plt.xlabel("Years (2000-2021)") # x axis label
        plt.ylabel("population") # y axis label
        
        plt.title("Population data graph") #graph title
        plt.show() #displays graph

 
if __name__ == '__main__':
    main()

print('Thank you for your input! Take care.')
