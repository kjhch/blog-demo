function request()
  return wrk.format("GET","/cache/user?id="..math.random(1,50000))
end