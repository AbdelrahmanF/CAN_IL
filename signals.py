import re

signal_name      = []
signal_frame_name= []
signal_start_bit = []
signal_length    = []
signal_factor    = []
signal_offset    = []
signal_min       = []
signal_max       = []

frame_ID   = []
frame_name = []
frame_DLC  = []

VAL_TABLE  = []
ENUM_TYPEDEF = []

dbc= open("C:/Users/Documents/Database.dbc","r")
fl =dbc.readlines()

def parse_signals(line):

	signal_line_pattern = "^\s+SG_\s"
	signal_name_pattern = "\sSG_\s\w+"
	signal_start_bit_pattern = ":\s\d+"
	signal_length_pattern = "\d+@"
	signal_factor_pattern = "\(\d+"
	signal_offset_pattern = ",(-\d+|\d+)"
	signal_min_pattern = "\[.+\|"
	signal_max_pattern = "\d+\]"
	

	
	index = 0
	#for line in fl:
	if re.search(signal_line_pattern, line):
		#print(line)	
		
		#signal name:
		m = re.search(signal_name_pattern, line)
		if(m):
			temp = re.sub(r"\sSG_\s", "", m.group(0))
			signal_name.append(temp)
		
		#start bit:
		m = re.search(signal_start_bit_pattern, line)
		if(m):
			temp = re.sub(r":\s", "", m.group(0))
			signal_start_bit.append(temp)
			
		#length: 
		m = re.search(signal_length_pattern, line)
		if(m):
			temp = re.sub(r"@", "", m.group(0))
			signal_length.append(temp)
		
		#factor:
		m = re.search(signal_factor_pattern, line)
		if(m):
			temp = re.sub(r"\(", "", m.group(0))
			signal_factor.append(temp)
			
		#offset:
		m = re.search(signal_offset_pattern, line)
		if(m):
			temp = re.sub(r",", "", m.group(0))
			signal_offset.append(temp)
			
		#Min:
		m = re.search(signal_min_pattern, line)
		if(m):
			temp = re.sub(r"\[", "", m.group(0))
			temp = re.sub(r"\|", "", temp)
			signal_min.append(temp)
			
		#Max:
		m = re.search(signal_max_pattern, line)
		if(m):
			temp = re.sub(r"\]", "", m.group(0))
			signal_max.append(temp)
		
		index = index + 1
	signal_frame_name.append(temp_ID)
	#print ('Number of signals is', index)

def main():
	global temp_ID
	frame_found = 0
	frame_line_pattern = "^BO_.+"
	
	frame_ID_pattern = "_\s\d+"
	frame_name_pattern = "\s\w+:"
	frame_DLC_pattern = ":\s\d\s"
	
	val_table_pattern = "VAL_TABLE_\s.+"
	enum_typedef_pattern = "VAL_TABLE_\s\w+"
	enum_id_value = '\d+\s\".+?"'

	
	frame_DLC 
	
	for i in range(0, len(fl)):
		
		ln = fl[i]
		if re.search(frame_line_pattern, ln):
			
			#frame ID:
			m = re.search(frame_ID_pattern, ln)
			if(m):
				temp = re.sub(r"_\s", "", m.group(0))
				temp = str(hex(int(temp)))
				frame_ID.append(temp)
				
			#frame name  \s\w+:
			m = re.search(frame_name_pattern, ln)
			if(m):
				temp = re.sub(r"\s", "", m.group(0))
				temp = re.sub(r":", "", temp)
				frame_name.append(temp)
				temp_ID = temp
				
			#DLC :\s\d\s
			m = re.search(frame_DLC_pattern, ln)
			if(m):
				temp = re.sub(r":\s", "", m.group(0))
				temp = re.sub(r"\s", "", temp)
				frame_DLC.append(temp)	
					
			#Cycle_ms
			#Direction
			#Tx_Type
			
			t_idx = i+1
			ln = fl[t_idx]
			
			while (not(fl[t_idx] in ['\n', '\r\n'])) and (t_idx < len(fl)):
				#print(t_idx)
				parse_signals(fl[t_idx])
				t_idx = t_idx + 1
			i = t_idx

		else:
			if re.search(val_table_pattern, ln):	#extract VAL_TABLE whole line
				#VAL_TABLE.append(ln)
				#print(ln)
				temp_line = "typedef enum{"+"\n"
				m = re.search(enum_typedef_pattern, ln)
				if(m):
					temp = re.sub(r"VAL_TABLE_ Enc_", "", m.group(0))	#remove the prefix to extract typedef name
					typedef = temp
					#ENUM_TYPEDEF.append(temp)
					#print(typedef)
				#VAL_TABLE.append("typedef enum{"+"\n")
				
				for match in re.finditer(enum_id_value, ln):		#extract enum + value
					#print(match.group(0))	#enum_id_value
					m = re.search(r'\d+', match.group(0))				#extract value
					if(m):
						name = re.sub(r"\d+\s\"", "", match.group(0))	#remove quotes and value from name		#\d+\s\"\w+\s\w+"
						name = re.sub(r"\"", "", name)	#remove quotes from name
						name = re.sub(r"\s+", "_", name)	#remove quotes from name
						name = typedef+"_"+name.upper()
						value = m.group(0)
						#print(name+"="+value)
					temp_line = temp_line+name+"="+value+",\n"
				
				temp_line = temp_line[:-2]	#remove last comma
				temp_line = temp_line+"\n}"+typedef+"_t"+";"
				#print(temp_line)
				VAL_TABLE.append(temp_line)				
				#print("\n")
	#print(VAL_TABLE)
	dbc.close()
	
	file = open("C:/Users/afahmy/Documents/config.txt","w")
	
	file.write("\n")
	file.write("/* TO BE COPIED TO CAN_cfg.c */\n")
	
	file.write("void init_frames(void){\n\n")

	for i in range(len(frame_ID)):
		file.write("CAN_Frames[%s].ID = %s;\n" % (frame_name[i] , frame_ID[i]))
		file.write("CAN_Frames[%s].DLC = %s;\n" % (frame_name[i] , frame_DLC[i]))
		file.write("\n")
	file.write("}\n")	
	
	file.write("\nvoid init_signals(void){\n\n")
	for i in range(len(signal_name)):
		file.write("CAN_Signals[%s].FrameID = %s;\n" % (signal_name[i] , signal_frame_name[i]))
		file.write("CAN_Signals[%s].Factor = %s;\n" % (signal_name[i] , signal_factor[i]))
		file.write("CAN_Signals[%s].Offset = %s;\n" % (signal_name[i] , signal_offset[i]))
		file.write("CAN_Signals[%s].StartBit = %s;\n" % (signal_name[i] , signal_start_bit[i]))
		file.write("CAN_Signals[%s].Length = %s;\n" % (signal_name[i] , signal_length[i]))
		file.write("CAN_Signals[%s].Min = %s;\n" % (signal_name[i] , signal_min[i]))
		file.write("CAN_Signals[%s].Max = %s;\n" % (signal_name[i] , signal_max[i]))
		file.write("\n")
	file.write("}\n")	
	
	file.write("\n")
	file.write("/* TO BE COPIED TO CAN_cfg.h */\n")
	
	file.write("\ntypedef enum{\n\n")
	for i in range(len(signal_name)):
#		file.write("%s = %d,\n" % (signal_name[i] , i))
		file.write("%s ,\n" % (signal_name[i]))
	file.write("MAX_NUM_SIGNALS}\n\nCAN_Signal_Names_t;\n")

	file.write("\ntypedef enum{\n\n")
	for i in range(len(frame_ID)):
#		file.write("%s = %d,\n" % (frame_name[i] , i))
		file.write("%s ,\n" % (frame_name[i] ))
	file.write("MAX_NUM_FRAMES}\n\nCAN_Frame_Names_t;\n")
	
	file.write("\n")

	for i in range(len(VAL_TABLE)):
		file.write("%s\n" % (VAL_TABLE[i] ))
		file.write("\n")
	file.close()
	
	
main()
