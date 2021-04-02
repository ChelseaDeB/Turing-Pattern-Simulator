#!/bin/bash


#if you have conda installed and sed not working than might have to type 
#conda install -c conda-forge sed' in your terminal to update sed

#This is to selecte a line and replace it from the python program 
#sed 's/ START OF THE LINE \(.*\)END OF THE LINE/WHAT THE NEW LINE WILL BE/' FILE_WE_ARE_EDITING

#Function that prints out the options that the user can do 

Options () {
	echo "Type 1 if you want to simulate a turing pattern that was seeded with an image"
	echo "Type 2 if you want to simulate a turing pattern that was randomly seeded or middle seed"
	echo "Type 3 if you want to simulate a time lapse of a turing pattern that was seeded with an image"
	echo "Type 4 if you want to simulate a time lapse of a turing pattern that was randomly seeded"
	echo "Type 0 if you want to exit"
}

ExitOrContinue () {
	echo "You have completed your task. Type 0 1 2 3 or 4 with regards to what you would like to do next."
	Options
}

InititalizeGraph() {
	echo "Input the diffusion coefficient of activator'"
	read Da
	echo "Input the diffussion coefficient of inhibitor'"
	read Di
	echo "Input the feed value"
	read Feed
	echo "Input the kill value"
	read Kill
}

Options
read RESPONSE

while [ $RESPONSE != "0" ]
	do

	if [ $RESPONSE == "1" ]
		then

		InititalizeGraph

		echo "Input the name of the file that will seed the simulation"
		read SeedPattern
		while ! [ -f $SeedPattern ]
			do 
			echo "File not in folder"			
			echo "Whats the name of the file that will seed the simulation?"
			read SeedPattern	
		done

		echo "Input the number of iterations that you want the simulation to run for"
		read Iter

		echo "Input the name of the file that the outputted image will be saved under"
		read FileName

		echo $Se

		./Simulate.py --Da $Da --Di $Di --F $Feed --K $Kill --SeedPat $SeedPattern --Ite $Iter --FileName $FileName

		ExitOrContinue
		read RESPONSE
		continue 
	fi

	if [ $RESPONSE == "2" ]
		then

		InititalizeGraph

		echo "Input \"Random\" or \"Mid\" depending on the method you want to seed with"
		read SeedPat
		while [ $SeedPat != "Random" ] && [ $SeedPat != "Mid" ]
			do
			echo "Invalid input. Must be \"Random\" or \"Mid\""
			read SeedPat
		done

		if [ $SeedPat == "Random" ]
			then
			echo "Input the number of seeds you want"
			read NumSeed
			echo "Input the radius for the seeds"
			read Radius
			echo "Input the number of iterations that you want the simulation to run for"
			read Iter
			echo "Input the name of the file that the outputted image will be saved under"
			read FileName

			./Simulate.py --Da $Da --Di $Di --F $Feed --K $Kill --SeedPat $SeedPat --Ite $Iter --FileName $FileName --Radius $Radius --NumSeed $NumSeed


		else

			echo "Input the radius for the seed"
			read Radius
			echo "Input the number of iterations that you want the simulation to run for"
			read Iter
			echo "Input the name of the file that the outputted image will be saved under"
			read FileName

			./Simulate.py --Da $Da --Di $Di --F $Feed --K $Kill --SeedPat $SeedPat --Ite $Iter --FileName $FileName --Radius $Radius 
		fi

		ExitOrContinue
		read RESPONSE
		continue 
	fi

	if [ $RESPONSE == "3" ]
		then 
		InititalizeGraph

		echo "Input the name of the file that will seed the simulation"
		read SeedPattern
		while ! [ -f $SeedPattern ]
			do 
			echo "File not in folder"			
			echo "Whats the name of the file that will seed the simulation?"
			read SeedPattern	
		done

		echo "Input the number of iterations that you want the simulation to run for"
		read Iter

		echo "Input the number of iterations between images"
		read Steps

		echo "Input the name of the file that the outputted images will be saved under"
		read FileName

		./SimulateOverlapse.py --Da $Da --Di $Di --F $Feed --K $Kill --SeedPat $SeedPattern --Ite $Iter --FileName $FileName --Steps $Steps
		
		ExitOrContinue
		read RESPONSE
		continue 
	fi
	if [ $RESPONSE == "4" ]
		then

		InititalizeGraph

		echo "Input \"Random\" or \"Mid\" depending on the method you want to seed with"
		read SeedPat
		while [ $SeedPat != "Random" ] && [ $SeedPat != "Mid" ]
			do
			echo "Invalid input. Must be \"Random\" or \"Mid\""
			read SeedPat
		done

		if [ $SeedPat == "Random" ]
			then
			echo "Input the number of seeds you want"
			read NumSeed
			echo "Input the radius for the seeds"
			read Radius
			echo "Input the number of iterations that you want the simulation to run for"
			read Iter
			echo "Input the number of iterations between images"
			read Steps
			echo "Input the name of the file that the outputted images will be saved under"
			read FileName

			./SimulateOverlapse.py --Da $Da --Di $Di --F $Feed --K $Kill --SeedPat $SeedPat --Ite $Iter --FileName $FileName --Radius $Radius --NumSeed $NumSeed --Steps $Steps


		else

			echo "Input the radius for the seed"
			read Radius
			echo "Input the number of iterations that you want the simulation to run for"
			read Iter
			echo "Input the number of iterations between images"
		read Steps
			echo "Input the name of the file that the outputted images will be saved under"
			read FileName

			./SimulateOverlapse.py --Da $Da --Di $Di --F $Feed --K $Kill --SeedPat $SeedPat --Ite $Iter --FileName $FileName --Radius $Radius --Steps $Steps
		fi
		
		ExitOrContinue
		read RESPONSE
		continue 

	else
		echo "Invalid input. Must be 0, 1, 2, or 3"
		Options
		read RESPONSE
		continue 
		

	fi
done

echo "You have exited the program."





	







	
