function sensorsdata2015jssdkcross(screen_height, screen_width, userAgent) {
  // Generate cookie value
  const randomId = Math.random().toString(36).substr(2, 10);
  return `sensorsdata2015jssdkcross={\\"distinct_id\\":\\"${randomId}\\",\\"first_id\\":\\"${randomId}\\"}`;
}