using UnrealBuildTool;

public class Movement : ModuleRules
{
	public Movement(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { 
			"Core", 
			"CoreUObject", 
			"Engine"
        });
		PrivateDependencyModuleNames.AddRange(new string[] { 
			
		});
	}
}
