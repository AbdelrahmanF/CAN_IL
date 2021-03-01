/*
 * CAN_cfg.c
 *
 *  Created on: May 19, 2020
 *      Author: Abdelrahman Fahmy
 */


#include "CAN_cfg.h"
#include "CAN_drv.h"

#ifndef UNIT_TEST
#include <PE_Types.h>
#include <stddef.h>
#include <stdtypes.h>
#else
/*#include "../../Generated_Code/PE_Types.h"*/
#include "C:/Unity/src/unity.h"
/*#include "C:/Freescale/CW MCU v11.0/MCU/S12lisa_Support/s12lisac/include/stddef.h"*/
#include "C:/Freescale/CW MCU v11.0/MCU/S12lisa_Support/s12lisac/include/stdtypes.h"
#ifndef TPE_Float
typedef float TPE_Float;
#endif
#endif


CAN_Signal_t CAN_Signals[MAX_NUM_SIGNALS];
CAN_Frame_t CAN_Frames[MAX_NUM_FRAMES];



void init_frames(void);
void init_signals(void);

/*
** ===================================================================
**     Method      :  init_frames
**     Description :
**         Initialise the frames parameters as per the dbc
**          
**     Parameters  :
**         NAME            - DESCRIPTION
**       	void		       
**                         
**     Returns     :
**         ---             void
** ===================================================================
*/
void init_frames(void)
{
	/*
	CAN_Frames[<Frame_Name>].Cycle_ms 	= CYCLIC_FRAME_20MS;
	CAN_Frames[<Frame_Name>].ID 		= 0x150;
	CAN_Frames[<Frame_Name>].Direction	= CAN_TX;
	CAN_Frames[<Frame_Name>].DLC 		= 2;
	CAN_Frames[<Frame_Name>].Tx_Type	= CYCLIC;*/
}

/*
** ===================================================================
**     Method      :  init_signals
**     Description :
**         Initialise the signals parameters as per the dbc
**          
**     Parameters  :
**         NAME            - DESCRIPTION
**       	void		       
**                         
**     Returns     :
**         ---             void
** ===================================================================
*/
void init_signals(void)
{
	
	/*CAN_Signals[<Signal_Name>].FrameID = <Frame_Name>;
	CAN_Signals[<Signal_Name>].Factor = 1;
	CAN_Signals[<Signal_Name>].Offset = 0;
	CAN_Signals[<Signal_Name>].StartBit = 0;
	CAN_Signals[<Signal_Name>].Length = 2;
	CAN_Signals[<Signal_Name>].Min = 0;
	CAN_Signals[<Signal_Name>].Max = 0;*/

}

/*
** ===================================================================
**     Method      :  CAN_cfg_init
**     Description :
**         Initialise the frames and signals parameters as per the dbc
**          
**     Parameters  :
**         NAME            - DESCRIPTION
**       	void		       
**                         
**     Returns     :
**         ---             void
** ===================================================================
*/
void CAN_cfg_init(void)
{
	init_frames();
	init_signals();
}
