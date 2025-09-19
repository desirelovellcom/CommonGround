"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export function ProtocolDiagram() {
  return (
    <div className="w-full max-w-4xl mx-auto">
      <Card className="bg-gray-900 border-gray-700">
        <CardHeader>
          <CardTitle className="text-white text-center">CommonGround Protocol Architecture</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Foundation Layer */}
            <div className="text-center">
              <div className="bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg p-6 mb-4">
                <h3 className="text-white font-bold text-lg">Foundation Layer</h3>
                <p className="text-blue-100 text-sm mt-2">L0 - Canonical Ledger</p>
              </div>
              <div className="space-y-2">
                <Badge className="bg-blue-900 text-blue-100">UTXOs & FC Issuance</Badge>
                <Badge className="bg-blue-900 text-blue-100">Anchor-Set Roots</Badge>
                <Badge className="bg-blue-900 text-blue-100">Identity Hashes</Badge>
              </div>
            </div>

            {/* Culture Layer */}
            <div className="text-center">
              <div className="bg-gradient-to-br from-green-500 to-teal-600 rounded-lg p-6 mb-4">
                <h3 className="text-white font-bold text-lg">Culture Layer</h3>
                <p className="text-green-100 text-sm mt-2">L1 - Sovereign Roll-ups</p>
              </div>
              <div className="space-y-2">
                <Badge className="bg-green-900 text-green-100">Culture Credits</Badge>
                <Badge className="bg-green-900 text-green-100">Local Policy</Badge>
                <Badge className="bg-green-900 text-green-100">Data Residency</Badge>
              </div>
            </div>

            {/* Personal Layer */}
            <div className="text-center">
              <div className="bg-gradient-to-br from-purple-500 to-pink-600 rounded-lg p-6 mb-4">
                <h3 className="text-white font-bold text-lg">Personal Layer</h3>
                <p className="text-purple-100 text-sm mt-2">L2 - User Devices</p>
              </div>
              <div className="space-y-2">
                <Badge className="bg-purple-900 text-purple-100">II-Agents</Badge>
                <Badge className="bg-purple-900 text-purple-100">Private Context</Badge>
                <Badge className="bg-purple-900 text-purple-100">Local Models</Badge>
              </div>
            </div>
          </div>

          {/* Flow Arrows */}
          <div className="mt-8 text-center">
            <div className="flex justify-center items-center space-x-4 text-gray-400">
              <span>Personal Layer</span>
              <span>↕</span>
              <span>Culture Layer</span>
              <span>↕</span>
              <span>Foundation Layer</span>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
