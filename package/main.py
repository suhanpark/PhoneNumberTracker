import tracker

if __name__ == '__main__':
	number = str(input("Insert your phone number with the country code/number\n"
	               "> "))

	try:
		info = tracker.phone_number_info(number)

		# number
		print("\nPhone Number:")
		print(info[0])

		# location
		print("\nLocation:", info[1])

		# carrier
		print("\nCarrier or Service Provider:", info[2])

		# time zone
		print("\nTime Zone:")
		for zone in info[3]:
			print(zone, "\n")

		# validity
		if info[4]:
			print("The phone number is valid")
		else:
			print("The phone number is invalid")

		# possibility
		if info[5]:
			print("The phone number is possible\n")
		else:
			print("The phone number is impossible\n")

		print("Processing Completed.")
	except:
		raise
		print("Error Occurred. Please check your input.")