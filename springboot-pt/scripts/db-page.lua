function request()
  return wrk.format("GET","/users?pageNum="..math.random(1,250000).."&pageSize=20")
end