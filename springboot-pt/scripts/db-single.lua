function request()
  return wrk.format("GET","/user?id="..math.random(1,5000000))
end