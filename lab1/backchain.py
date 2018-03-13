from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    # find rules that produces this hypothesis
    rules_con = [hypothesis]

    for rule in rules:
        for con in rule.consequent():
            bindings = match(con, hypothesis)

            if(bindings != None):
                # this rule can result in the hypo
                ant = rule.antecedent()

                if(isinstance(ant, AND)):
                    rules_con.append(AND([backchain_to_goal_tree(rules, populate(branch, bindings)) for branch in ant]))
                elif(isinstance(ant, OR)):
                    rules_con.append(OR([backchain_to_goal_tree(rules, populate(branch, bindings)) for branch in ant]))
                else:
                    rules_con.append(backchain_to_goal_tree(rules, populate(ant, bindings)))

    return simplify(OR(rules_con))

# Here's an example of running the backward chainer - uncomment
# it to see it work:
# print backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin')
