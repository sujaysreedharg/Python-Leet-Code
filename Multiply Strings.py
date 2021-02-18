class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product  = [0 for i in range(len(num1)+len(num2))]
        n1= num1[::-1]
        n2= num2[::-1]
        for i in range(len(n1)):
            for j in range(len(n2)):
                product[i+j]+= int(n1[i])*int(n2[j])
                if product[i+j]>=10:
                    carry,digit = divmod(product[i+j],10)
                    product[i+j]= digit
                    product[i+j+1]+= carry
        while len(product)>1 and product[-1]==0:
            product.pop()
        result = "".join(str(x) for x in reversed(product))
        return result
                    
