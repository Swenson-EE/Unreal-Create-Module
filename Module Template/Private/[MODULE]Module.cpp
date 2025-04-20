#include "[MODULE]Module.h"
#include "[MODULE].h"


IMPLEMENT_MODULE([MODULE]Module, [MODULE]);



/* This will get called when the editor loads the module */
void [MODULE]Module::StartupModule()
{
	UE_LOG(Log[MODULE], Display, TEXT("[MODULE] Module has started"));
}

/* This will get called when the editor unloads the module */
void [MODULE]Module::ShutdownModule()
{
	UE_LOG(Log[MODULE], Display, TEXT("[MODULE] Module has shutdown"));
}

