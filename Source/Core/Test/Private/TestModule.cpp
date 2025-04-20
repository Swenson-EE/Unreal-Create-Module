#include "TestModule.h"
#include "Test.h"


IMPLEMENT_MODULE(TestModule, Test);



/* This will get called when the editor loads the module */
void TestModule::StartupModule()
{
	UE_LOG(LogTest, Display, TEXT("Test Module has started"));
}

/* This will get called when the editor unloads the module */
void TestModule::ShutdownModule()
{
	UE_LOG(LogTest, Display, TEXT("Test Module has shutdown"));
}

