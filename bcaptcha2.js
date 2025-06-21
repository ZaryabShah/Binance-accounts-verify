function jt(dist, bizId, data, userAgent, platform, validateId, clientInterHeight, clientOuterHeight, clientW, clientH, centerX, centerY) {
  // Simplified implementation
  const timestamp = Date.now();
  return JSON.stringify({
    bizId: bizId,
    dist: dist,
    userAgent: userAgent,
    platform: platform,
    validateId: validateId,
    clientInterHeight: clientInterHeight,
    clientOuterHeight: clientOuterHeight,
    clientW: clientW,
    clientH: clientH,
    centerX: centerX,
    centerY: centerY,
    timestamp: timestamp
  });
}