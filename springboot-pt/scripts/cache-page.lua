function request()
  return wrk.format("GET","/cache/users?pageNum="..math.random(1,2500).."&pageSize=20")
end