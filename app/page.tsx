"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { ProtocolDiagram } from "@/components/protocol-diagram"
import { ProofOfBenefit } from "@/components/proof-of-benefit"

export default function CommonGroundHome() {
  const [selectedComponent, setSelectedComponent] = useState<string | null>(null)

  const components = [
    {
      id: "foundation-coins",
      name: "Foundation Coins",
      description: "Intelligence-backed currency minted through Proof-of-Benefit",
      color: "bg-gradient-to-br from-yellow-200 to-yellow-400",
      details:
        "Every Foundation Coin is collateralized by verifiable public benefit - data curation, model training, or inference serving.",
    },
    {
      id: "ii-agents",
      name: "II-Agents",
      description: "Sovereign AI assistants bound to non-custodial wallets",
      color: "bg-gradient-to-br from-purple-200 to-purple-400",
      details:
        "Each citizen receives one II-Agent that runs under their key, providing open and verifiable intelligence.",
    },
    {
      id: "national-champions",
      name: "National Champions",
      description: "Validator franchises running compute clusters",
      color: "bg-gradient-to-br from-orange-200 to-orange-400",
      details: "Twelve Champions at launch, expanding to one per sovereign nation, securing the Foundation layer.",
    },
    {
      id: "anchor-sets",
      name: "Anchor-Sets",
      description: "Auditable data provenance roots on-chain",
      color: "bg-gradient-to-br from-green-200 to-green-400",
      details: "Merkle roots of datasets, models, and agent identities provide tamper-evident history.",
    },
    {
      id: "culture-credits",
      name: "Culture Credits",
      description: "Local jurisdiction currency for sovereign roll-ups",
      color: "bg-gradient-to-br from-blue-200 to-blue-400",
      details: "Each Champion maintains a roll-up with local CC units, respecting data-residency rules.",
    },
    {
      id: "guardian-sentinels",
      name: "Guardian Sentinels",
      description: "Network monitoring and security agents",
      color: "bg-gradient-to-br from-indigo-200 to-indigo-400",
      details: "Specialized II-Agents that monitor runtime logs, meter energy, and replay PoB receipts.",
    },
    {
      id: "oracle-council",
      name: "Oracle Council",
      description: "Fifteen-seat governance body using CommonGround protocol",
      color: "bg-gradient-to-br from-pink-200 to-pink-400",
      details: "Parameter governance through Partner-grade II-Agents orchestrating micro-teams of specialists.",
    },
  ]

  return (
    <div className="min-h-screen bg-black text-white">
      {/* Header */}
      <header className="border-b border-gray-800 bg-gradient-to-r from-gray-900 to-black">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
            CommonGround
          </h1>
          <p className="text-gray-300 mt-2">Interactive Protocol Interface - Intelligent Internet Architecture</p>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        <Tabs defaultValue="components" className="w-full">
          <TabsList className="grid w-full grid-cols-3 bg-gray-800">
            <TabsTrigger value="components" className="text-gray-300">
              Components
            </TabsTrigger>
            <TabsTrigger value="architecture" className="text-gray-300">
              Architecture
            </TabsTrigger>
            <TabsTrigger value="consensus" className="text-gray-300">
              Consensus
            </TabsTrigger>
          </TabsList>

          <TabsContent value="components" className="space-y-6">
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {components.map((component) => (
                <Card
                  key={component.id}
                  className="bg-gray-900 border-gray-700 hover:border-gray-600 transition-all cursor-pointer transform hover:scale-105"
                  onClick={() => setSelectedComponent(component.id)}
                >
                  <CardHeader>
                    <div className={`w-full h-20 rounded-lg ${component.color} mb-4 flex items-center justify-center`}>
                      <div className="w-12 h-12 bg-black/20 rounded-lg"></div>
                    </div>
                    <CardTitle className="text-white">{component.name}</CardTitle>
                    <CardDescription className="text-gray-400">{component.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <Badge variant="secondary" className="bg-gray-800 text-gray-300">
                      CommonGround Component
                    </Badge>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* Selected Component Details */}
            {selectedComponent && (
              <Card className="bg-gray-900 border-gray-700">
                <CardHeader>
                  <CardTitle className="text-white">
                    {components.find((c) => c.id === selectedComponent)?.name}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-300 mb-4">{components.find((c) => c.id === selectedComponent)?.details}</p>
                  <Button
                    onClick={() => setSelectedComponent(null)}
                    variant="outline"
                    className="border-gray-600 text-gray-300 hover:bg-gray-800"
                  >
                    Close Details
                  </Button>
                </CardContent>
              </Card>
            )}
          </TabsContent>

          <TabsContent value="architecture">
            <ProtocolDiagram />
          </TabsContent>

          <TabsContent value="consensus">
            <ProofOfBenefit />
          </TabsContent>
        </Tabs>

        {/* Footer Info */}
        <div className="mt-12 text-center">
          <h2 className="text-2xl font-bold text-white mb-4">The CommonGround Protocol</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">
            A Bitcoin for the Intelligence Age - building sovereign AI through permissionless coordination, anchored on
            auditable open-licensed datasets with Proof-of-Benefit consensus.
          </p>
          <div className="mt-6 flex justify-center gap-4">
            <Badge className="bg-gradient-to-r from-blue-500 to-purple-500">Open Source</Badge>
            <Badge className="bg-gradient-to-r from-green-500 to-blue-500">Verifiable Public Benefit</Badge>
            <Badge className="bg-gradient-to-r from-purple-500 to-pink-500">Credible Neutrality</Badge>
          </div>
        </div>
      </main>
    </div>
  )
}
