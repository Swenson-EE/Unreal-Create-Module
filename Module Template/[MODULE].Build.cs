using UnrealBuildTool;

public class [MODULE] : ModuleRules
{
	public [MODULE](ReadOnlyTargetRules Target) : base(Target)
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
