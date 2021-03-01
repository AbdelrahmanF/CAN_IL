/*
 * CAN_drv.h
 *
 *  Created on: May 18, 2020
 *      Author: Abdelrahman Fahmy
 */

#ifndef CAN_DRV_H_
#define CAN_DRV_H_

/*
 * *****************************************************************
 * INCLUDE
 * *****************************************************************
 */
#include "CAN_cfg.h"
#ifndef UNIT_TEST
#include <PE_Types.h> 
#include <stddef.h>
#include <stdtypes.h>
#else
/*#include "../../Generated_Code/PE_Types.h"*/
#include "C:/Unity/src/unity.h"
/*#include "C:/Freescale/CW MCU v11.0/MCU/S12lisa_Support/s12lisac/include/stddef.h"*/
#include "C:/Freescale/CW MCU v11.0/MCU/S12lisa_Support/s12lisac/include/stdtypes.h"
#include "./test/stubs.h"

#ifndef TPE_Float
typedef float TPE_Float;
#endif

#endif

/*
 * *****************************************************************
 * DEFINE
 * *****************************************************************
 */
#define CYCLIC_FRAME_15MS	15
#define CYCLIC_FRAME_20MS	20

#define CAN_GetSysTick()						System_GetTick()

/*
 * *****************************************************************
 * DATA TYPES
 * *****************************************************************
 */

/********** Frame Properties *************************************/
typedef struct
{
	uint32_t				LastSystick;
	uint16_t 				ID;
	uint8_t 				DLC;
	CAN_Frame_Direction_t 	Direction;
	CAN_Frame_TX_TYPE_t   	Tx_Type;
	uint8_t 				Cycle_ms;
	uint8_t					Data[8U];
	uint8_t					Prev_Data[8U];
}CAN_Frame_t;


/********** Signal Properties *************************************/
typedef struct
{
	/* dynamic */
	int32_t 			PhysicalValue;
	
	/* static members */
	TPE_Float 			Factor;
	uint16_t 			Init;/*for Tx only*/
	int16_t 			Offset;
	int16_t 			Min;
	int16_t 			Max;
	CAN_Frame_Names_t 	FrameID;
	uint8_t 			StartBit;
	uint8_t 			Length;
	CAN_SIGNAL_SIGN_t	Sign;
	int8_t				bits_in_byte_1;
	int8_t				bits_in_byte_2;
	uint8_t 			start_byte;
	
}CAN_Signal_t;



/*
 * *****************************************************************
 * INTERFACE
 * *****************************************************************
 */
void CAN_drv_init(void);
void CAN_drv_run(void);


#endif /* CAN_DRV_H_ */

