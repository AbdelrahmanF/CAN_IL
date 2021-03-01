/*
 * CAN_cfg.h
 *
 *  Created on: May 19, 2020
 *      Author: Abdelrahman Fahmy
 */

#ifndef CAN_CFG_H_
#define CAN_CFG_H_


void CAN_cfg_init(void);


/*
 * *****************************************************************
 * Signals
 * *****************************************************************
 */
typedef enum
{
	//<Signal_Name> = 0,
	MAX_NUM_SIGNALS
}CAN_Signal_Names_t;

/*
 * *****************************************************************
 * Frames
 * *****************************************************************
 */
typedef enum
{
	//<Frame_Name> = 0	,
	MAX_NUM_FRAMES
}CAN_Frame_Names_t;

typedef enum
{
	UNDEFINED_DIR = 0,
	CAN_TX		 	 ,
	CAN_RX
}CAN_Frame_Direction_t;

typedef enum
{
	NONE = 0	,
	CYCLIC		,
	TRIGGERED	
}CAN_Frame_TX_TYPE_t;

typedef enum
{
	UNSIGNED = 0	,
	SIGNED	
}CAN_SIGNAL_SIGN_t;

#endif /* CAN_CFG_H_ */

