local function requireany(...)
    local errs = {}
    for _, name in ipairs {...} do
        if type(name) ~= 'string' then
            return name, ''
        end
        local ok, mod = pcall(require, name)
        if ok then
            return mod, name
        end
        errs[#errs + 1] = mod
    end
    error(table.concat(errs, '\n'), 2)
end

-- Try to use whatever bit-manipulation library that is available
local bit, _ = requireany('bit', 'nixio.bit', 'bit32', 'bit.numberlua')

function str_to_arr(str, arr)
    local data = arr or {}
    if str then
        for i = 1, #str do
            print(i .. " => " .. string.byte(str, i))
            data[#data + 1] = string.byte(str, i)
            print(table.concat(data, ", "))
        end
    end

    return data
end

function test2(b, c)
    return b + c
end

function test(a, d, callback)
    v = 20
    return callback(a, d) + v

end

function byte2bin(n)
    local t, d = {}, 0
    d = math.log(n) / math.log(2) -- binary logarithm
    for i = math.floor(d + 1), 0, -1 do
        t[#t + 1] = math.floor(n / 2 ^ i)
        n = n % 2 ^ i
    end
    return table.concat(t)
end

print(test(2, 4, test2))

-- print(str_to_arr("~SerialNumber,DateTime"))

local n = 10
local m = 2
print(n .. " ==> " .. byte2bin(n))
print(m .. " ==> " .. byte2bin(m))
print(n .. " & " .. m .. " ==> " .. bit.band(n, m))
print("Byte to bin : " .. n .. " & " .. m .. " ==> " .. byte2bin(bit.band(n, m)))

print(m .. " lshift ==> " .. bit.lshift(m, 8))
print(m .. " rshift ==> " .. bit.rshift(m, 8))
print()

local bin = "0000001000000000"

bin = string.reverse(bin)
local sum = 0

for i = 1, string.len(bin) do
    num = string.sub(bin, i, i) == "1" and 1 or 0
    sum = sum + num * math.pow(2, i - 1)

end

print(sum)

print(tonumber("0000001000000000", 2))

for i = 0, 7 do
    print(i)
end

print(" multi expression :*****************************************")

for i = 0, 10, 2 do
    print(i)
end
