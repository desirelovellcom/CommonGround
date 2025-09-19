"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"

export function ProofOfBenefit() {
  const [selectedBenefit, setSelectedBenefit] = useState<string | null>(null)

  const benefitClasses = [
    {
      id: "compute-inference",
      name: "Compute-Inference",
      description: "Serving end-user requests for models in public registry",
      progress: 85,
      color: "from-yellow-400 to-orange-500",
    },
    {
      id: "compute-training",
      name: "Compute-Training",
      description: "Training or fine-tuning models on auditable data",
      progress: 72,
      color: "from-green-400 to-blue-500",
    },
    {
      id: "data-curation",
      name: "Data-Curation",
      description: "Running II-Commons pipeline: deduplication, contamination checks",
      progress: 91,
      color: "from-purple-400 to-pink-500",
    },
    {
      id: "agent-orchestration",
      name: "Agent-Orchestration",
      description: "II-Agent execution traces with ≥3 module rule",
      progress: 67,
      color: "from-blue-400 to-indigo-500",
    },
  ]

  return (
    <Card className="bg-gray-900 border-gray-700">
      <CardHeader>
        <CardTitle className="text-white">Proof-of-Benefit Classes</CardTitle>
        <p className="text-gray-400">Foundation Coins are minted only when verifiable public benefit is performed</p>
      </CardHeader>
      <CardContent>
        <div className="grid gap-4">
          {benefitClasses.map((benefit) => (
            <div key={benefit.id} className="space-y-3">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="text-white font-medium">{benefit.name}</h4>
                  <p className="text-gray-400 text-sm">{benefit.description}</p>
                </div>
                <Badge className={`bg-gradient-to-r ${benefit.color} text-white`}>{benefit.progress}% Active</Badge>
              </div>
              <Progress value={benefit.progress} className="h-2" />
            </div>
          ))}
        </div>

        <div className="mt-6 p-4 bg-gray-800 rounded-lg">
          <h5 className="text-white font-medium mb-2">PoB Receipt Structure</h5>
          <div className="text-sm text-gray-300 space-y-1">
            <div>
              <span className="text-blue-400">work_root:</span> Merkle root of inputs/outputs
            </div>
            <div>
              <span className="text-green-400">benefit_class:</span> Type of benefit performed
            </div>
            <div>
              <span className="text-yellow-400">eval_score:</span> Numeric evaluation score
            </div>
            <div>
              <span className="text-purple-400">producer_id:</span> Champion public key hash
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
