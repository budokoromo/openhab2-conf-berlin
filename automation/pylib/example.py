scriptExtension.importPreset("RuleSupport")
scriptExtension.importPreset("RuleSimple")


class myRule(SimpleRule):
    def execute(self, module, inputs):
        print "Hello World from Jython"

sRule = myRule()
sRule.setTriggers([Trigger("aTimerTrigger", "timer.GenericCronTrigger", Configuration({"cronExpression": "0/15 * * * * ?"}))])

automationManager.addRule(sRule)


