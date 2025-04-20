#include "MovementModule.h"
#include "Movement.h"


IMPLEMENT_MODULE(MovementModule, Movement);



/* This will get called when the editor loads the module */
void MovementModule::StartupModule()
{
	UE_LOG(LogMovement, Display, TEXT("Movement Module has started"));
}

/* This will get called when the editor unloads the module */
void MovementModule::ShutdownModule()
{
	UE_LOG(LogMovement, Display, TEXT("Movement Module has shutdown"));
}

