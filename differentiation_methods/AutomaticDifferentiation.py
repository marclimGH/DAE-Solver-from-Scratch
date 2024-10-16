from math import sin,cos, exp

def sin_backprop_rule(x):
    y = sin(x)
    def sin_pullback(y_cotangent):
        x_cotangent = y_cotangent*cos(x)
        return x_cotangent       
    return y,sin_pullback

def exp_backprop_rule(x):
    y = exp(x)
    def exp_pullback(y_cotangent):
        x_cotangent = y_cotangent*exp(x)
        return x_cotangent       
    return y,exp_pullback

#dictionary that relate functions to their back propagation rule
primitive_rules = {
    sin: sin_backprop_rule,
    exp: exp_backprop_rule,
}

#vector jacobian product
def vjp(chain, primal):
    
    #primal pass, goes through each operation in the chain and saves the pullback accordigly
    #pullback chain
    pulllback_stack = []
    current_value = primal  #primal position where we want to evaluate tha chain 
    #Primal Pass
    for operation in chain:
        rule = primitive_rules[operation]   # e.g. get the rule for the sin 
        current_value, current_pullback = rule(current_value) # e.g return sin(current_value), sin_pullback
        pulllback_stack.append(current_pullback)
    
    #Reverse Pass
    def pullback(cotangent):
        current_cotangent = cotangent
        for backFunction in reversed(pulllback_stack):
            current_cotangent = backFunction(current_cotangent)
        print(backFunction)
        return current_cotangent
    
    return current_value, pullback


def val_and_grad(chain, x):
    y, back = vjp(chain,x)
    derivative = back(1.0)
    return y, derivative


test_chain = [sin, sin, exp] # exp(sin(sin(x)))
test_x =2.0
f_x,pullback = vjp(test_chain, test_x)

###forward
## current_value = exp(  sin(    sin(    x)))
# x3 = sin(sin(x))
# x2 = sin(x)
# x1 = x
# this x3,x2,x1 are stored as a value
###backward
##  exp_pullback(y_cotangent) = y_cotangent*exp(x)
##  sin_pullback(y_cotangent) = y_cotangent*cos(x)   
# pullback(cotangent) = exp_pullback( sin_pullback ( sin_pullback ( cotangent ))) 
# pullback(cotangent) = sin_pullback ( sin_pullback ( cotangent )) * exp( x3 )
# pullback(cotangent) = sin_pullback ( cotangent ) *cos (x2 ) * exp( x3 )
# pullback(cotangent) = cotangent * cos(x1) *cos (x2 ) * exp( x3 )
# pullback(cotangent) = cotangent * cos(x) *cos (sin(x)) * exp(sin(sin(x)))
# x = 2
# pullback(1) = 1 * cos(x) *cos (sin(x)) * exp(sin(sin(x)))
print( cos(2) *cos (sin(2)) * exp(sin(sin(2)))  ) 
print( pullback(2.0)   )

f_x, df_x =val_and_grad(test_chain, test_x)
print(f_x)
print(df_x)

f = lambda x: exp(sin(sin(x)))
print(f(2))

df = lambda x: exp(sin(sin(x)))*cos(sin(x))*cos(x)
print(df(2))

test_CHAIN = [[sin, sin, exp], # exp(sin(sin(x)))
              [exp, sin, sin], # sin(sin(exp(x)))
              [exp, sin, exp]] # exp(sin(exp(x)))  
test_X = [2.0,2.0,2.0]

# Loop over each chain and its corresponding input
for chain, x in zip(test_CHAIN, test_X):
    F_x, Grad_x = val_and_grad(chain, x)
    print(f"Chain: {chain}, Input: {x}")
    print(f"Function value: {F_x}, Gradient: {Grad_x}")


