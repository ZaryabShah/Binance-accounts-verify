function jt(distance, bizId, data, userAgent, platform, clientInterHeight, clientOuterHeight, slideX, slideY) {
  // Simplified implementation
  const timestamp = Date.now();
  return JSON.stringify({
    bizId: bizId,
    distance: distance,
    userAgent: userAgent,
    platform: platform,
    clientInterHeight: clientInterHeight,
    clientOuterHeight: clientOuterHeight,
    slideX: slideX,
    slideY: slideY,
    timestamp: timestamp
  });
}