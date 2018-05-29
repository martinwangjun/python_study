import collections
class MemberCounter:
    print('我不在def中，但是我被打印了')
    members = 0
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)

m1.members = 'Ten'
print(m2.members)

print(MemberCounter.__base__) # 结果：<class 'object'>
# python允许多重继承，所以基类可以不止一个
print(MemberCounter.__bases__) # 结果：(<class 'object'>,)

print(issubclass(dict, collections.OrderedDict))
print(issubclass(collections.OrderedDict, dict))
print(isinstance('dd', str))
print(m1.__class__)

print(callable(print))

